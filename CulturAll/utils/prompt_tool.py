def prompt_sqa(sample):
    return f"""
    Using the scenario as context, answer the question in as few words as possible.
    Scenario: {sample["scenario"]}
    Question: {sample["question"]}
    Answer:
    """


def prompt_sqa_eng(sample):
    return f"""
    Using the scenario as context, answer the question in as few words as possible.
    Scenario: {sample["english_scenario"]}
    Question: {sample["english_question"]}
    Answer:
    """


def prompt_eval(sample, prediction):
    return f"""
    Evaluate the accuracy of the model prediction based on the provided scenario, question, ground truth answer, and explanation.

    Scenario: {sample["scenario"]}
    Question: {sample["question"]}
    Answer: {sample["answer"]}
    Explanation: {sample["explanation"]}

    Model prediction: {prediction}

    Output only 1 or 0 without any additional text:
    Output 1 if the model prediction matches the ground truth answer and aligns with the explanation.
    Output 0 if the model prediction does not match the ground truth answer or fails to align with the explanation.
    """


def prompt_eval_eng(sample, prediction):
    return f"""
    Please evaluate whether the model prediction is correct based on the given scenario, question, answer, and explanation.

    Scenario: {sample["english_scenario"]}
    Question: {sample["english_question"]}
    Answer: {sample["english_answer"]}
    Explanation: {sample["english_explanation"]}

    Model prediction: {prediction}

    Only output 1 or 0 with no additional text. 1 means correct, 0 means incorrect.
    """


def prompt_grounded_existing_datasets(sample, topic_list=None):
    return f"""
    You are given a sample describing some cultural knowledge with topic as {sample["source_topic"]} (may not be provided):

    {sample["source_excerpt"]}

    From the topic list {topic_list}, select the most appropriate topic, and then generate a real-world sample (scenario + question + answer + explanation) 
    to assess the consultant's grasp of the cultural knowledge.
    Ensure the generated sample preserves the same cultural knowledge as the provided example. Do not modify the choices or the correct answer.
    The generated sample should be in the same language as the given sample.

    The output format should be:
    [Topic]
    one topic from the topic list
    [Scenario]
    XXX
    [Question]
    XXX
    [Answer]
    XXX
    [Explanation]
    XXX
    Do not output any other things.
    """


def prompt_grounded_online_resources(sample):
    return f"""
    You are given a sample describing some cultural knowledge:

    {sample["response"]}

    Generate a real-world sample (scenario + question + answer + explanation) 
    to assess the consultant's grasp of the cultural knowledge.
    Ensure the generated sample preserves the same cultural knowledge as the provided example.
    The answer should be objective and as brief as possible. If an objective free-form answer is impractical, convert the question to a four-option multiple-choice format (A–D) and return only the chosen letter.
    The generated sample should be in the same language as the given sample.

    The output format should be:
    [Scenario]
    XXX
    [Question]
    XXX
    [Answer]
    XXX
    [Explanation]
    XXX
    Do not output any other things.
    """


def prompt_mt(source, target_language):
    return f"""
    Translate the following text to {target_language}.:

    {source}

    Do not output any other things.
    """


def prompt_country_code(row):
    return f"""
    Based on the following text and its written language,
    retrieve the corresponding ISO 3166-1 alpha-2 country code (only one lowercase two-letter country code).

    Scenario: {row["scenario"]}
    Question: {row["question"]}

    Do not output any other things.
    """
