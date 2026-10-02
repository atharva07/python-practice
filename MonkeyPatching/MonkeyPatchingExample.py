# Without monkey patching
def get_data():
    return "real data"

def process():
    return get_data() + "Process"

# Using Monkey Patching
def test_process(monkeypatch):
    def get_fake_data():
        return "mock data"
    
    monkeypatch.setattr("app.get_data", get_fake_data)

import os
def get_env():
    return os.getenv("ENV")

def test_process(monkeypatch):
    def set_env():
        return "QA Env"
    
    monkeypatch.setenv("ENV", set_env)

    assert get_env() == "QA"

def set_data():
    return "real data"

def test_process(monkeypatch):
    def set_fake_data():
        return "mock data"
    
    monkeypatch.setattr("app.set_data", set_fake_data)