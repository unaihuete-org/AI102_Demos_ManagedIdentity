# AI102_ManagedIdentity
Calling Cognitive Service from Azure Function using Managed Identity (MSI)


1. Create an Azure Function App and Cognitive Service.
3. Enable System Assigned MSI for Azure Function.
4. In the Azure Function Configuration settings add a new **Application Setting** called **CognitiveServicesEndpoint**, containing the endpoint of your Cognitive Service.
5. In the Cognitive Service resource, add the MSI to role **Cognitive Services User** in **Access Control**.
6. Clone the repo and publish the function.
