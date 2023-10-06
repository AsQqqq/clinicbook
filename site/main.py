from route import upload_route, app


if __name__ == "__main__":
    """Запуск кода"""
    if upload_route():
        print("Flask started")
    app.run(debug=True, host="localhost", port="3040")