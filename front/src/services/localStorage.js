
export function getRestaurantName() {
        const userJson = localStorage.getItem("auth");
        const user = JSON.parse(userJson);
        return user.name
    } 
export function getRestaurantId() {
    const userJson = localStorage.getItem("auth");
    const user = JSON.parse(userJson);
    return user.id_restaurant;
  }
