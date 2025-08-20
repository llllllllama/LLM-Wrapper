from llm_wrapper import LLMWrapper
llm_wrapper = LLMWrapper()
# Test the LLMWrapper class
def test_llm_wrapper():
    try:
        # Test with a simple prompt
        prompt = "What is the capital of France?"
        response = llm_wrapper.ask(prompt)
        print("Response:", response)
        
        # Check if the response is not empty
        assert response, "Response should not be empty"
        
        # Check if the response contains expected content
        assert "Paris" in response, "Response should contain 'Paris'"
        
        print("Test passed successfully!")
    except ValueError as e:
        print(f"Test failed: {e}")



    # run the test
    test_llm_wrapper()
