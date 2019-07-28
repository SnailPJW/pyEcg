# pyEcg
demo:
![demo ecg figure](https://github.com/SnailPJW/pyEcg/blob/master/EcgGrid.PNG)

Steps:

| 步驟 | 指令 | 說明 |
| --- | --- | --- |
| 1. | 無 | Open Colab (Click this: https://colab.research.google.com/drive/1RH0_pu6y496kxf4HVxyCW3bcpUTQd2Tn) |
| 2. | !ls | 來查看目前工作目錄下有哪些東西(第一次執行應該會看到當下目錄下有一個資料夾為"sample_data") |
| 3. | !mkdir demo | 新增一個名為 demo 的資料夾 |
|  . | %cd demo | 目前工作目錄的指標移動到指向 demo 資料夾 |
|  . | !pwd | 查看目前工作目錄為何 |
| 4. | !git clone $url_git_HTTPS | 下載此份專案到目前工作目錄下 |
|  . | !ls | 可以看到目前工作目錄下出現了 pyEcg 資料夾 |
|  . | %cd pyEcg | 移動到 pyEcg 資料夾中 |
|  . | !ls | 可以看到專案中的所有檔案了，包括 sqlite 的DB檔案 |
| 5. | 無 | 執行 cell 中的 python 程式碼就可以看到 Output 結果 |
|  . | 無 | xxx |


------
Research:
1. Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network (https://stanfordmlgroup.github.io/projects/ecg2/)
2. wfdb-python (https://github.com/MIT-LCP/wfdb-python)
3. EEGrunt update: Analyze heart rate and HRV with Python (http://www.autodidacts.io/analyze-ecg-heart-rate-and-hrv-with-python-and-eegrunt/)
4. PhysioBank Databases (http://www.physionet.org/physiobank/database/)
------
1. Reading and plotting informations record data. (https://www.pybytes.com/pywfdb/example-drawing.html)
2. BioSPPy - Biosignal Processing in Python. (https://pypi.org/project/biosppy/)
3. Machine Learning for medicine: QRS detection in a single channel ECG signal (Part 1: data-set creation) (https://medium.com/@roszcz/machine-learning-for-medicine-qrs-detection-in-a-single-channel-ecg-signal-part-1-data-set-be36f70bbd38)
------
Ref:
1. Working with Binary Data in Python (https://www.devdungeon.com/content/working-binary-data-python)
2. https://www.scadacore.com/tools/programming-calculators/online-hex-converter/
3. https://gregstoll.com/~gregstoll/floattohex/
4. Reading a Blob from SQLite database(https://www.reddit.com/r/learnpython/comments/98u08d/reading_a_blob_from_sqlite_database/)
5. convert binary string to numpy array (https://stackoverflow.com/questions/11760095/convert-binary-string-to-numpy-array)

