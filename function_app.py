import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="alert_http", methods=["POST"])
def AlertHttp(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("AlertHttp function triggered")

    try:
        body = req.get_json()
    except ValueError:
        logging.error("Invalid JSON received")
        return func.HttpResponse(
            "Invalid JSON",
            status_code=400
        )

    essentials = body.get("data", {}).get("essentials", {})
    alert_rule = essentials.get("alertRule", "unknown")
    severity = essentials.get("severity", "unknown")

    # 🔴 THIS LOG LINE IS WHAT YOUR QUERY MATCHES
    logging.warning(
        f"ALERT FIRED | rule={alert_rule} | severity={severity}"
    )

    return func.HttpResponse(
        json.dumps({
            "status": "accepted",
            "alert": alert_rule,
            "severity": severity
        }),
        status_code=200,
        mimetype="application/json"
    )
