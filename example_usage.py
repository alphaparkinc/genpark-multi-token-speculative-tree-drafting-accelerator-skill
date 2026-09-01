from client import MultiTokenSpeculativeTreeDraftingAcceleratorClient

def main():
    client = MultiTokenSpeculativeTreeDraftingAcceleratorClient()
    res = client.draft_speculative_token_tree(4096, 5, 6)
    print('Speculative Tree Drafting: ' + res['drafting_session_id'])
    print('Accepted Tokens/Step: ' + str(res['accepted_tokens_per_step_mean']) + ' | Speedup: ' + str(res['inference_throughput_speedup_x']) + 'x')
    print('KV Verification Passed: ' + str(res['exact_kv_verification_passed']))

if __name__ == '__main__':
    main()
