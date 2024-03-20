import React, { useState } from "react";
import { Link } from "react-router-dom";
import house_door from "@img/house-door.svg";
import person from "@img/person-circle.svg";
import "./Header.scss";

import Authorization from "@components/Authorization/Authorization";

const Header: React.FC = () => {
  const [isVisible, setIsVisible] = useState<boolean>(false);
  const [userName, setUserName] = useState<string>("");

  const action = (_userName:string) => {
    console.log(userName)
    console.log("action", _userName)
    setUserName(_userName);
  }

  const User = () => {

    const localStorageUser = JSON.parse(localStorage.getItem("currentUser") as string);
    console.log(Boolean(userName || localStorageUser?.username))
    const UserName = userName || localStorageUser?.username;

    return <div
      onClick={() => setIsVisible(!isVisible)}
      className="persone position-relative"
    >
      {UserName ? UserName : "Войти"}
      <img src={person} />
      <span className="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
        99+
        <span className="visually-hidden">unread messages</span>
      </span>
    </div>
  };

  return (
    <>
      <header
        className="
    sticky-top
    Header"
      >
        <nav className="hstack gap-3 ">
          <Link className="p-2 text-decoration-none" to="/">
            <img src={house_door} />
            Главная страница
          </Link>

          <div className="p-2 ms-auto text-decoration-none hideOnMobile">
              <User />            
          </div>
          
        </nav>
      </header>
      {isVisible && (
        <div className="Popup">
          <div id="content">
            <Authorization setUserName={action}/>
          </div>
        </div>
      )}
    </>
  );
};

export default Header;
