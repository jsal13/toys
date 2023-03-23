from typing import Dict, Any

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/echo")
def echo_response(resp: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Echos respose.

    You can test this with something like:

    ```bash
    curl -X POST http://localhost:8002/echo /
    -H "Content-Type: application/json" /
    -d '{"data": "whats up"}'
    ```

    """
    print(resp)
    return resp


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
