import string
from flask import Flask, request,jsonify
import psycopg2

app = Flask(__name__) # setup initial flask app; gets called throughout in routes

#change to run
conn_params = {
        "host":"db_IP",
        "database": "lab1-2",
        "user":"user",
        "password":"password",
        "port": "5432"
}


# New route
@app.route('/polygon', methods=['GET'])
def get_polygon():
    try:
        conn=psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        query = """
            SELECT jsonb_build_object(
                'type', 'feature',
                'geometry', ST_AsGeoJSON(geom)::jsonb,
                'properties', jsonb_build_object('id',id)
            )
            FROM polygon
            LIMIT 1;
        """

        cursor.execute(query)
        polygon_geojson = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return jsonify(polygon_geojson)

    except Exception as e:
        return jsonify({"error": str(e)}), 500



# route only prints data to console
@app.route('/print_data', methods=['POST'])
def print_data():
  
  print("*********************")
  print("*********************")
  print(request.method) # finds method -> here it should be "POST"
  print(request.data) # generic - get all data; covers case where you don't know what's coming
  print(request.json) # parses json data
  print("*********************")
  print("*********************")
  return "Accepted 202 - post received; printed to console"

if __name__ == "__main__":
    app.run(
      #debug=True, #shows errors 
      host='0.0.0.0', #tells app to run exposed to outside world
      port=5000)
