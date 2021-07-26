# AI102_ManagedIdentity
Calling Cognitive Service from Azure Function using Managed Identity


1. Create System Assigned MSI for Azure Function
1. In the Azure Function Configuration settings add a new **Application Setting** called **CognitiveServicesEndpoint**, containing the endpoint of your Cognitive Service.
1. In the Cognitive Service resource, add the MSI with role **Cognitive Services User** in **Access Control**.
