import requests
from mcp.server.fastmcp import FastMCP
mcp = FastMCP('MealDB Server')

BASE_URL = 'https://www.themealdb.com/api/json/v1/1'

@mcp.tool()
def search_meals_by_name(name: str) -> str:
    """Search for a meal recipe by name. Returns ingredients and instructions."""
    res= requests.get(f'{BASE_URL}/search.php', params={'s': name})
    data= res.json()

    if not data["meals"]:
        return f"No meals found for '{name}'"
    
    meal = data["meals"][0]  # Just return the first match for simplicity
    ingredients = []
    for i in range(1, 21):
        ing = meal.get(f'strIngredient{i}')
        measure = meal.get(f'strMeasure{i}')
        if ing and ing.strip():
            ingredients.append(f"{measure.strip()} {ing.strip()}")      
    return f"""Meal: {meal['strMeal']}
Category: {meal['strCategory']}
Cuisine: {meal['strArea']}
Ingredients: {', '.join(ingredients)}
Instructions: {meal['strInstructions'][:500]}...
"""
@mcp.tool()
def list_categories() -> str:
    """List all meal categories."""
    res = requests.get(f'{BASE_URL}/categories.php')
    data = res.json()
    categories = [cat['strCategory'] for cat in data['categories']]
    return "Meal Categories:\n" + "\n".join(categories)

@mcp.tool()
def random_meal() -> str:
    """Get a random meal recipe."""
    res = requests.get(f'{BASE_URL}/random.php')
    data = res.json()
    meal = data['meals'][0]
    return f"""Random Meal: {meal['strMeal']}"""

if __name__ == '__main__':
    mcp.run()

