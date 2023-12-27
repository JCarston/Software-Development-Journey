# Morning Health Check

The MHC(Morning Health Check) script pulls alerts from Opsgenie, adjusts the response, and formats/injects that formatted data into ServiceNow. Here is a guide to get the script running

* Modify the variable `get_Opsgenie_URL` within the `opsgenie_list_view` function. Adjust the limit to be the number of recently closed alerts you want to pull.
* Modify the variable `servicenow_url` within the `service_now_noce_creation` function. Change the NOCE number to the one you want (These NOCEs are manually created within ServiceNow).
* Modify the string `SOMETHINGWASHERE` with the correct credentials found within Thycotic

Once the script runs, it will display the JSON response in the console log of all the alerts it could pull and give a counter on how many records were created.


## API Information

* Opsgenie "Get Alert" Documentation: https://docs.opsgenie.com/docs/alert-api
* ServiceNow "Rest Explorer" Documentation: https://docs.servicenow.com/bundle/vancouver-api-reference/page/integrate/inbound-rest/concept/use-REST-API-Explorer.html
