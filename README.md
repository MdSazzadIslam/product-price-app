### E-commerce Dashboard Solution

### Project Description
```
The goal is to develop a dashboard for the sales and marketing department to display various Key Performance Indicators (KPIs) related to product sales. The dashboard should be visually appealing and suitable for presentation to the management team. Key features include:

```    

### Charts:
- Sales Trend Over Time:
    - Line graph showcasing sales trends over specific periods (daily, monthly, quarterly, annually) to understand growth trends and seasonal changes.

- Sales by Region:
    - Geographic heat map visualizing sales performance across different regions.

- Sales by Category:
    - Pie chart or bar graph illustrating sales distribution across various product categories.

- Top Selling Products:
    - Horizontal bar graph displaying the top 10 (or a chosen number) best-selling products.

- Sales vs. Target:
    - Bar graph with actual sales and target sales for each product/category.


- Customer Demographics:
    - Graphs breaking down sales by customer demographics such as age, gender, occupation, etc.

- Revenue and Profit Analysis:
    - Line graphs or bar graphs showing revenue, costs, and profit over time.

- Sales Conversion Rate:
    - Percentage of site visitors or leads that convert into sales, depicted over time or across marketing channels.

### Tech stacks
```
This project utilizes the following technologies:

Node.js: JavaScript runtime
TypeScript: Static type-checking
Apollo Server: GraphQL server
Express: Web framework for Node.js
MongoDB: NoSQL database
Jest: Testing framework

```

### Running the application   

#  Environment variable
Ensure the following environment variables are set:

```
PORT=8000
DB_URL=mongodb://localhost:27017/salesDashboard
NODE_ENV=development
CLIENT_ORIGIN=http://localhost:3000

```
# Running locally
```
If you are running the application without Docker, make sure that MongoDB is installed and running on your local machine. You can typically start MongoDB using the following command:

mongod

```
# scripts
1. Seed the Database
```
npm run seed

```
2. Start the Application in the Development Mode
```
npm run dev

```

3. Run Unit Tests
```
npm run test

```

# Deployment 
To deploy the application using Docker:

```
docker-compose up -d

```
