**How to build**: 
<p>I. <b>Install Solr</b>:</p>
    <ul><li> docker run -p 8983:8983 -t solr </li> </ul>

<p>II. <b>FastAPI</b>:</p>
    1. Create an venv
    <ul>
        <li>python3 -m venv upsell-env</li>
        <li>source upsell-env/bin/activate</li>
    </ul>
    2. Install dependency</br>
    <ul><li> pip3 install -r requirements.txt </li> </ul>
    3. Run</br>
    <ul>
        <li> cd app/ </li>
        <li> uvicorn main:app --reload </li>
    </ul>

<p>III. <b>Running on</b>:</p>
    <ul>
        <li> API Endpoint: http://127.0.0.1:8000 </li>
        <li> Interactive API docs: http://127.0.0.1:8000/docs </li>
        <li> Alternative API docs: http://127.0.0.1:8000/redoc </li>
    </ul>

