import React from "react";


const Login = () => {

    const handleLogin = () => {
        console.log('Login');
    };

    return (
        <div>
            <h1>Авторизация</h1>
            <form>
                <input type="text" placeholder="Логин" />
                <input type="password" placeholder="Пароль" />
                <button onClick={handleLogin}>Войти</button>
            </form>
        </div>
    );
};