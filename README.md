#IoT Controlador de Calidad del Aire (2020)

Se crearon dispositivos IoT virtuales vía AWS (AWS IoT & DynamoDB), conectados a la [API de IQAir AirVisual](https://www.iqair.com/air-pollution-data-api), que detectan la calidad del aire en muchos lugares del mundo. Para esto, se ocupó DynamoDB para almacenar los datos, para luego llamarlos y desplegar la calidad del aire de diferentes oficinas de una empresa a través de una Web App. El objetivo era crear un sistema que prende los filtros de aquellas oficinas automáticamente, dependiendo del índice AQI. 
 
> Virtual IoT devices were created via AWS (AWS IoT & DynamoDB), connected to the [IQAir AirVisual API](https://www.iqair.com/air-pollution-data-api), which detect air quality in many parts of the world. For this, DynamoDB was used to store the data, to then call them and display the air quality of different offices of a company through a Web App. The objective was to create a system that turns on the filters of those offices automatically, depending on the AQI index.

<img width="784" alt="airfilter_demo" src="https://user-images.githubusercontent.com/31099183/116835008-95b05880-ab8e-11eb-972f-96ca7ddea546.png">
<img width="939" alt="airfilter_aqui" src="https://user-images.githubusercontent.com/31099183/116835021-a3fe7480-ab8e-11eb-81ef-7e72f74cf9b3.png">
