import config from "@/config.js";
import {getRestaurantId} from "@/services/localStorage.js";





export async function getListOfMenus() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: getRestaurantId(),
    },
  };
  const response = await fetch(`${config.API_PATH}/menus`, settings);
  const listOfMenus = await response.json();
  return listOfMenus;
}

export async function getMenuByDate(date) {
  const settings = {
    method: "GET",
    headers: {
      Authorization: getRestaurantId(),
    },
  };
  const response = await fetch(
    `${config.API_PATH}/menus/by-date/` + date,
    settings
  );
  const menus = await response.json();
  return menus;
}

export async function getMenuModify() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: getRestaurantId(),
    },
  };
  const response = await fetch(
    `${config.API_PATH}/menus/` + localStorage.id_menu,
    settings
  );
  const dict_plates = await response.json();
  return dict_plates;
}

export async function updateMenu(menu) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(menu),
    headers: {
      Authorization: getRestaurantId(),
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/menus`, settings);
}
export async function getMenuToday(name_restaurant) {
  const response = await fetch(
    `${config.API_PATH}/menu-today/`+name_restaurant
  );
  if (response.status == 404 ){
    return 404
  }
  else{
    const menu = await response.json();
    return menu;
  }
}
