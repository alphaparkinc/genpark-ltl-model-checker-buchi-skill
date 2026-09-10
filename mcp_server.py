from client import LTLPathValidator
import json

def handle_request(req):
    ltl = LTLPathValidator()
    action = req.get("action")
    if action == "check":
        formula = req.get("formula", ())
        trace = [set(t) for t in req.get("trace", [])]
        res = ltl.check_trace(formula, trace)
        return {"status": "ok", "holds": res}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "check", "formula": ["F", ["prop", "ack"]], "trace": [["init"], ["ack"]]})))
