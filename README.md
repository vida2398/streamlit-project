# 📊 Data Analysis Website: Automotive Fuel Efficiency Explorer

## 1. Project Overview

| Category | Description |
| :--- | :--- |
| **Topic** | **Building an Interactive Website for Automotive Fuel Efficiency Data Analysis** |
| **Reason for Topic Selection** | The goal was to utilize automotive data to create a **user-friendly, interactive web environment** using Streamlit. This platform allows users to visualize analysis results and explore data based on custom criteria, demonstrating the ability to build a practical data analysis tool. |
| **Data Analysis Content** | The project uses the `mpg.csv` dataset to perform the following analyses: |
| | - **Comparative Visualization of City Average MPG (cty) by Manufacturer** (using Matplotlib/Seaborn and Plotly). |
| | - **Deep Dive Analysis** allowing users to select grouping variables, target columns (`cty` or `hwy`), and aggregation methods (`mean`, `max`, `min`) for custom data exploration. |

---

## 2. 🚀 Website Links and Demonstration

* **External URL (Streamlit Cloud Deployment Link):**
    * [Insert your Streamlit Cloud Deployment URL here]
* **Demonstration Video (YouTube):**
    * [Insert your YouTube Demonstration Video Link here]

---

## 3. 👨‍💻 Team Introduction

| Role | Name | GitHub Account |
| :--- | :--- | :--- |
| Team Member 1 | Cha Eun-woo | [@eunwoo\_cha](https://github.com/eunwoo_cha) |
| Team Member 2 | Byeon Woo-seok | [@wooseok\_byeon](https://github.com/wooseok_byeon) |
| ... | ... | ... |

---

## 4. 📝 Code and Execution Environment

### 4.1. Technologies and Libraries Used

* **Python**
* **Streamlit** (Web Dashboard Framework)
* **Pandas** (Data Manipulation)
* **Seaborn/Matplotlib** (Static Visualization)
* **Plotly Express** (Interactive Visualization)

### 4.2. How to Run the Website Locally

1.  **Clone the Repository:**
    ```bash
    git clone [Your GitHub Repository URL]
    cd [repository-folder-name]
    ```
2.  **Set Up Environment:**
    * Install the required libraries listed in `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```
3.  **Execute Streamlit App:**
    ```bash
    streamlit run 1104.py
    ```

### 4.3. Key Code Functionality

> Highlighting the main functions from your `1104.py` file.

**`show_car` Function (Manufacturer Average MPG Analysis):**

```python
def show_car():
    # ... data loading and preprocessing
    mpg = mpg.groupby("manufacturer", as_index=False).agg(avg_cty = ("cty","mean"))
    
    # Visualization using Plotly
    c1 = px.bar(data_frame=mpg, x = "manufacturer", y = "avg_cty")
    st.plotly_chart(c1)

def show_car_deep():
    # ... user selection for analysis parameters
    input1 = st.selectbox("Group By Column", mpg.columns)
    input2 = st.selectbox("Calculate Target", ['cty', 'hwy'])
    input3 = st.selectbox("Calculation Method", ["mean", "max", "min"])
 
    # Performing analysis based on user input
    result5 = mpg.groupby(input1).agg(value = (input2, input3))
    st.dataframe(result5)
