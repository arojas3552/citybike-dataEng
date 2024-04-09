# tests for streamlit ran with pytest

from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py", default_timeout=1000)
at.run()

#def test_title_area():
#  assert "City Bikes Interactive World Map" in at.title[0].value