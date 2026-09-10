from client import LTLPathValidator

def main():
    print("=== Testing LTL Path Validator ===")
    ltl = LTLPathValidator()
    
    trace = [{'init'}, {'request'}, {'request', 'ack'}, {'done'}]
    print(f"System Trace: {trace}")

    # Check F(ack) - eventually acknowledged
    f_ack = ltl.check_trace(('F', ('prop', 'ack')), trace)
    print(f"Property F(ack): {f_ack}")
    assert f_ack is True

    # Check G(done) - always done
    g_done = ltl.check_trace(('G', ('prop', 'done')), trace)
    print(f"Property G(done): {g_done}")
    assert g_done is False
    print("=== LTL Verification Complete ===")

if __name__ == "__main__":
    main()
