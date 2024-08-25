from flask import Flask, render_template, Response
from mask_detector import MaskDetector

app = Flask(__name__)

# Initialize the MaskDetector class
mask_detector = MaskDetector()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

def generate_frames():
    """Generate frames from the mask detector for video streaming."""
    while True:
        frame = mask_detector.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
