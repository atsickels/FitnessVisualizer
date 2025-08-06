import sqlite3

_session = None

def getSession():
    global _session
    if _session is None:
        _session = sqlite3.connect('./data/visualizer.db')
    return _session

def shutdown():
    global _session
    if _session is not None:
        _session.close()
        _session = None
        
    
