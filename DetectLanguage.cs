using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Azure.AI.TextAnalytics;
using Azure.Identity;

namespace Company.Function
{
    public static class DetectLanguage
    {
        [FunctionName("DetectLanguage")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "get", "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("C# HTTP trigger function processed a request.");

            string text = req.Query["text"];

            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);
            text = text ?? data?.text;
            log.LogInformation($"Sentence to detect language from: {text}");


            //Get language from sentence
            // Create client using endpoint and key

            //AzureKeyCredential credentials = new AzureKeyCredential(cogSvcKey);
            string cogSvcEndpoint = Environment.GetEnvironmentVariable("CognitiveServicesEndpoint");
            log.LogInformation($"CS endpoint used: {cogSvcEndpoint}");
    
            Uri endpoint = new Uri(cogSvcEndpoint);
            //var client = new TextAnalyticsClient(endpoint, credentials);
            var client = new TextAnalyticsClient(endpoint, new DefaultAzureCredential());

            // Call the service to get the detected language
            DetectedLanguage detectedLanguage = client.DetectLanguage(text);
            //return(detectedLanguage.Name);



            string responseMessage = string.IsNullOrEmpty(text)
                ? "This HTTP triggered function executed successfully. Pass a sentence  in the query string or in the request body for a estimated language response."
                        : $"Sentence: {text}. Predicted language: {detectedLanguage.Name}.";

                    return new OkObjectResult(responseMessage);
        }
    }
}
