import React, { useState } from "react";
import { Form, useNavigate } from "react-router-dom";
import "./Authorization.scss";

interface AuthorizationState {
  pending: boolean;
  state: string;
  isError: boolean;
}

interface AuthorizationProps {
  setUserName: (username: string) => void;
}

const Authorization: React.FC<AuthorizationProps> = ({ setUserName }) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [state, setState] = useState<AuthorizationState>({
    pending: false,
    state: "",
    isError: false,
  });

  const navigate = useNavigate();

  const localStorageUser = JSON.parse(
    localStorage.getItem("currentUser") as string
  );

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      setState({ pending: true, state: "Авторизация...", isError: false });
      const response = await (
        await fetch(
          "http://192.168.0.34:8000/users/authenticate/user-password",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              username,
              password,
            }),
          }
        )
      ).json();

      if (response.detail) {
        setState({
          pending: false,
          state: "Ошибка авторизации",
          isError: true,
        });
        return;
      }

      setState({
        pending: false,
        state: "Успешная авторизация",
        isError: false,
      });

      const currentUser = await (
        await fetch("http://192.168.0.34:8000/users/me", {
          headers: {
            Authorization: `Bearer ${response.access_token}`,
          },
        })
      ).json();

      localStorage.setItem("currentUser", JSON.stringify(currentUser));

      localStorage.setItem("access_token", response.access_token);

      if (typeof setUserName === "function") {
        setUserName(currentUser.username);
      } else {
        navigate("/");
      }
    } catch (error) {
      setState({
        pending: false,
        state: "Ошибка авторизации",
        isError: true,
      });
      console.log(error);
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center authorization">
      {!localStorageUser && (
        <div>
          <h5>Авторизация</h5>
          <Form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="username">Логин:</label>
              <input
                type="text"
                className="form-control"
                id="username"
                value={username}
                onChange={handleUsernameChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Пароль:</label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Войти
            </button>
            {state.pending && <div>Загрузка...</div>}
            {state.state && (
              <div className={state.isError ? "text-danger" : "text-success"}>
                {state.state}
              </div>
            )}
          </Form>
        </div>
      )}

      {localStorageUser && (
        <div>
          <h5>Привет, {localStorageUser.username}</h5>
          <li>Телефон: {localStorageUser.phone}</li>
          <li>Email: {localStorageUser.email}</li>
          <button
            className="btn btn-primary"
            onClick={() => {
              localStorage.clear();
              console.log(setUserName, typeof setUserName)
              if (typeof setUserName === "function") {
                setUserName("Войти");
                navigate("/");
              } else {
                navigate("/");
              }
            }}
          >
            Выйти
          </button>
        </div>
      )}
    </div>
  );
};

export default Authorization;
