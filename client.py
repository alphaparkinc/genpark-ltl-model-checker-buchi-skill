class LTLPathValidator:
    """
    Linear Temporal Logic (LTL) Path & Trace Validator.
    Evaluates temporal modal formulas over finite discrete state traces.
    """
    def check_trace(self, formula, trace):
        op = formula[0]
        if op == "prop":
            return formula[1] in trace[0] if trace else False
        elif op == "X":
            return self.check_trace(formula[1], trace[1:]) if len(trace) > 1 else False
        elif op == "F":
            for i in range(len(trace)):
                if self.check_trace(formula[1], trace[i:]):
                    return True
            return False
        elif op == "G":
            for i in range(len(trace)):
                if not self.check_trace(formula[1], trace[i:]):
                    return False
            return True
        elif op == "U":
            p1, p2 = formula[1], formula[2]
            for i in range(len(trace)):
                if self.check_trace(p2, trace[i:]):
                    if all(self.check_trace(p1, trace[j:]) for j in range(i)):
                        return True
            return False
        return False
