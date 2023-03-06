import os
from datetime import datetime, timedelta, timezone
# import XRay SDK libraries
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware



class UserActivities:

  def __init__(self, request):
        #self.xray_recorder = xray_recorder
        self.request = request
  
  def run(self, user_handle):
    # Start a segment 
    # xray ---
    segment = xray_recorder.begin_segment('user_activities')
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results
      
    # Start a subsegment
    subsegment = xray_recorder.begin_subsegment('mock-data')

    # xray ---
    dict = {
      "now": now.isoformat(),
      "results-size": len(model['data']) 
    }

    subsegment.put_metadata('key', dict, 'namespace')

    return model