# 🧠 Brainstormers

Built with **LangChain** and **Streamlit**, this tool enhances your brainstorming experience by offering curated, optimized chains inspired by real-world effective brainstorming techniques. Rather than using ChatGPT directly, this app allows you to engage with structured brainstorming methods, guiding you to explore ideas comprehensively and maximize the benefits of LLM-driven brainstorming.

This app provides various brainstorming techniques:
- **[Big Mind Mapping](https://arxiv.org/abs/2310.19275)**: Expands ideas across a wide scope, ideal for when you need to gather a maximum number of ideas.
- **[Reverse Brainstorming](https://info.orchidea.dev/innovation-blog/guide-to-ai-powered-brainstorming-sessions)**: Identifies ways to create a problem, revealing potential pitfalls and fostering innovative solutions.
- **[Role Storming](https://www.psychologytoday.com/us/blog/the-digital-self/202403/how-ai-can-transform-brainstorming)**: Encourages adopting different perspectives to gather diverse insights.
- **[SCAMPER](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-scamper)**: Applies the SCAMPER technique (Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse) to prompt unique ideas.
- **[Six Thinking Hats](https://www.groupmap.com/portfolio/six-thinking-hats)**: Based on Edward de Bono’s method, examines ideas from six angles: Data, Emotions, Risks, Benefits, Creativity, and Process Management.
- **[Starbursting](https://lucidspark.com/blog/how-to-use-starbursting-for-brainstorming)**: Generates questions using the 5 W's and 1 H (Who, What, Where, When, Why, How), offering in-depth topic exploration.

## Project Pipeline
The app’s pipeline is streamlined: instead of using agents or Langraph, it runs specific chains based on the selected brainstorming method. Each method initiates a structured chain tailored to the user’s choice. The output is organized into a tree of ideas, with an initial layer of ideas followed by deeper expansions as per each method's principles. For example, the Starbursting method generates detailed questions for each initial idea, followed by answers.
![Screenshot from 2024-11-02 20-51-40](https://github.com/user-attachments/assets/a703a222-2e5d-41ea-a7f9-be9a94add57a)

Results are presented as a hierarchical tree of ideas:
```python
class TreeNode:
    def __init__(self, idea):
        self.idea = idea
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
```

## Video Demo

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Azzedde/brainstormers
   ```
2. **Navigate to the project directory**:
   ```bash
   cd brainstormers
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**:
   ```bash
   streamlit run ./app.py
   ```

## Roadmap
Future improvements include:
- [ ] Streamable output for real-time interaction
- [ ] Deployment on HuggingFace
- [ ] Integration with local LLMs
- [ ] Optimized runtime for Big Mind Mapping

## Cost
This app is cost-effective, with Big Mind Mapping sessions costing around $0.01 per session, making it accessible and powerful for brainstorming needs.

Enjoy enhanced brainstorming and generate powerful ideas with our Brainstorming App!
