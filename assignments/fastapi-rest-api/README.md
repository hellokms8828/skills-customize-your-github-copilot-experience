# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create endpoints, handle HTTP methods, work with request/response models, and understand API design principles. This assignment covers the fundamentals of building scalable web services in Python.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application and create basic endpoints that respond to different HTTP methods (GET, POST). Implement a simple in-memory data store to manage resources and return appropriate responses.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create a GET endpoint to retrieve all resources
- Create a GET endpoint to retrieve a specific resource by ID
- Create a POST endpoint to add new resources
- Return data in JSON format with appropriate HTTP status codes
- Handle basic error cases (e.g., resource not found returns 404)


### 🛠️ Implement Data Validation and Models

#### Description
Define request and response models using Pydantic to validate and structure data. This ensures type safety, automatic documentation, and clear API contracts.

#### Requirements
Completed program should:

- Define Pydantic models for request/response data
- Validate incoming data with proper error messages
- Use models for type hints in endpoint functions
- Generate automatic API documentation (Swagger UI)
- Return 422 status code for validation errors
- Document models with field descriptions and examples


### 🛠️ Add Update and Delete Operations

#### Description
Extend the API with PUT and DELETE endpoints to provide full CRUD (Create, Read, Update, Delete) functionality. Implement proper state management and return meaningful responses.

#### Requirements
Completed program should:

- Create a PUT endpoint to update existing resources
- Create a DELETE endpoint to remove resources
- Validate that resources exist before updating/deleting
- Return 204 (No Content) for successful deletions
- Return 200 with updated data for successful updates
- Handle edge cases (updating non-existent resource, deleting non-existent resource)
