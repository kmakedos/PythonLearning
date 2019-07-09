from daemons import ui,dispatcher

if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.start()
    ui = ui.UI()
    ui.start()