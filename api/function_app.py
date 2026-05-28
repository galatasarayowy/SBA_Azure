import json
import math
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="CalculateArea", methods=["POST", "OPTIONS"])
def calculate_area(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "OPTIONS":
        return func.HttpResponse(status_code=204)

    try:
        data = req.get_json()
        shape = data.get("shape")

        if shape == "triangle":
            base = float(data.get("base"))
            height = float(data.get("height"))
            area = 0.5 * base * height
        elif shape == "square":
            side = float(data.get("side"))
            area = side ** 2
        elif shape == "circle":
            radius = float(data.get("radius"))
            area = math.pi * (radius ** 2)
        else:
            return func.HttpResponse(
                json.dumps({"error": "Invalid shape. Use triangle, square, or circle."}),
                status_code=400,
                mimetype="application/json"
            )

        return func.HttpResponse(
            json.dumps({"shape": shape, "area": round(area, 4)}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as exc:
        return func.HttpResponse(
            json.dumps({"error": str(exc)}),
            status_code=400,
            mimetype="application/json"
        )
