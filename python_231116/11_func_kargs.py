def hello_names(**msg):
    for i in msg:
        print(f"{msg[i]}! {i}")

hello_names(최인규 = "안녕하세요", Steve = "Hello", 다나카 = "고니찌와")