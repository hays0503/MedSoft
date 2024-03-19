import React, { useState } from 'react';
import './Authorization.scss';

const Authorization: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setPassword(event.target.value);
    };

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Perform authorization logic here
    };

    return (
        <div className="d-flex justify-content-center align-items-center Authorization">
            <div>
                <h5>Авторизация</h5>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="username">Логин:</label>
                        <input type="text" className="form-control" id="username" value={username} onChange={handleUsernameChange} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Пароль:</label>
                        <input type="password" className="form-control" id="password" value={password} onChange={handlePasswordChange} />
                    </div>
                    <button type="submit" className="btn btn-primary">Войти</button>
                </form>
            </div>
        </div>
    );
};

export default Authorization;