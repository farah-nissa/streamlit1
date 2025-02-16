Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import steamlit as st
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import steamlit as st
ModuleNotFoundError: No module named 'steamlit'
>>> import streamlit as st
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> st.title("Line Plot Practice")
2025-02-17 00:19:13.459 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:19:14.182 WARNING streamlit: 
  [33m[1mWarning:[0m to view a Streamlit app on a browser, use Streamlit in a file and
  run it with the following command:

    streamlit run [FILE_NAME] [ARGUMENTS]
2025-02-17 00:19:14.195 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
DeltaGenerator()
>>> data = pd.dataFrame({
...     "x": [1, 2, 3, 4],
...     "y": [10, 20, 30, 40]})
...                      
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data = pd.dataFrame({
AttributeError: module 'pandas' has no attribute 'dataFrame'. Did you mean: 'DataFrame'?
>>> data = pd.DataFrame({
...     "x": [1, 2, 3, 4],
...     "y": [10, 20, 30, 40]})
>>> plt.plot(data["x"], data["y"])
[<matplotlib.lines.Line2D object at 0x000002A0E1B62210>]
>>> st.pyplot()
2025-02-17 00:20:56.840 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:20:56.874 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:20:56.896 
Calling `st.pyplot()` without providing a figure argument has been deprecated
and will be removed in a later version as it requires the use of Matplotlib's
global figure object, which is not thread-safe.

To future-proof this code, you should pass in a figure as shown below:

```python
fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
# other plotting actions...
st.pyplot(fig)
```

If you have a specific use case that requires this functionality, please let us
know via [issue on Github](https://github.com/streamlit/streamlit/issues).

2025-02-17 00:20:56.925 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:20:57.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:20:57.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
DeltaGenerator()
num_points = st.slider("Number of points", min_value=100, max_value=1000, value=500, step=100)
2025-02-17 00:22:09.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:09.474 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:09.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:09.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:09.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
text_input = st.text_input("Enter some text: ")
2025-02-17 00:22:38.608 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:38.657 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:38.688 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:38.725 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:38.752 Session state does not function when running a script without `streamlit run`
2025-02-17 00:22:38.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:22:38.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
st.write("The name: ", text_input)
2025-02-17 00:23:02.236 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:02.286 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:02.314 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:02.327 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
show_plot = st.checkbox("Show plot", value=True)
2025-02-17 00:23:29.141 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:29.200 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:29.215 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:29.226 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:23:29.242 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
if not show_plot:
    plt.close()

plot_color = st.selectbox("Plot color", ["blue", "red", "green"])
2025-02-17 00:24:43.443 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:24:43.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:24:43.519 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:24:43.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:24:43.557 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:24:43.577 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
plt.plot(data["x"], data["y"], color=plot_color)
[<matplotlib.lines.Line2D object at 0x000002A0E1CCF390>]
st.camera_input("Take a picture")
2025-02-17 00:25:27.852 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:25:27.876 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:25:27.894 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:25:27.911 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-02-17 00:25:27.928 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
st.progress(progress_variable_1_to_100)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    st.progress(progress_variable_1_to_100)
NameError: name 'progress_variable_1_to_100' is not defined
st.progress("progress_variable_1_to_100")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    st.progress("progress_variable_1_to_100")
  File "C:\Users\ASUS\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\streamlit\elements\progress.py", line 147, in progress
    progress_proto.value = _get_value(value)
  File "C:\Users\ASUS\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\streamlit\elements\progress.py", line 78, in _get_value
    raise StreamlitAPIException(
streamlit.errors.StreamlitAPIException: Progress Value has invalid type: str
