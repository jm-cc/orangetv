import flask
import orange

IP_ORANGETV = "tvorange.home"
PORT = 5000
MAPPING = "default_mapping.yaml"

app = flask.Flask("Orange")
tv = orange.OrangeTV(IP_ORANGETV)
tv.load_channel_mapping(MAPPING)

purge = ["sur"] # Spurious words can be added by the vocal assistant.

def sanitize(string):
    res = string.lower()
    for w in purge:
        if res.startswith(w):
            res=res[len(w):]
    return res.strip()

@app.route("/switchoff")
def switch_off():
    tv.switch_off()
    return f""

@app.route("/channel/<channel_id>")
def switch_to_n(channel_id):
    tv.type_channel_id(channel_id)
    return f"Switched to {channel_id}"

@app.route("/channel_name", methods=["POST"])
def switch_to_name():
    data = sanitize(flask.request.data.decode())
    tv.switch_over_name(data)
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
