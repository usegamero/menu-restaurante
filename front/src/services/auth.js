import config from "@/config.js";



export async function login(id_restaurant, password ) {
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id_restaurant: id_restaurant,
            password: password,
            
            
        }),
        

    };


    const response = await fetch(`${config.AUTH_PATH}/login`, settings);
    return response
}
