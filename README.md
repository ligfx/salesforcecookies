```python
import salesforcecookies
import simple_salesforce

instance_url, session_id = salesforcecookies.get_instance_url_and_session()
sf = simple_salesforce.Salesforce(instance_url=instance_url, session_id=session_id)
```
