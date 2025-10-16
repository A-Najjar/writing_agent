import streamlit as st
from writing_agent.main import agent_executor, parser

# Set up the Streamlit app
st.set_page_config(page_title="AI Research Assistant", page_icon="📘")

# Title and description
st.title("📘 AI Research Assistant")
st.write("Enter your research topic and let the AI agent gather structured results for you.")

# Input field for research topic
query = st.text_input("Research Topic", "")

# Run Research button
if st.button("Run Research"):
    if query.strip():
        with st.spinner("Running research, please wait..."):
            try:
                # Call the agent
                raw_response = agent_executor.invoke({"query": query})
                structured_response = parser.parse(raw_response.get("output")[0]["text"])

                # Display the results
                st.header("Research Results")
                st.subheader("Topic")
                st.write(structured_response.topic)

                st.subheader("Summary")
                st.write(structured_response.summary)

                st.subheader("Sources")
                st.write("\n".join([f"- {source}" for source in structured_response.sources]))

                st.subheader("Tools Used")
                st.write(", ".join(structured_response.tools_used))
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a research topic.")