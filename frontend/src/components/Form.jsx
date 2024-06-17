import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css"
// import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit =  (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            const res =  api.post(route, { username, password }) 
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, res?.data?.access);
                localStorage.setItem(REFRESH_TOKEN, res?.data?.refresh);
                navigate("/")
            } else {
                navigate("/login")
            }
        } catch (error) {
            if (error.response) {
            // Server responded with a status other than 200 range
            alert(`Error: ${error.response.status} - ${error.response.data}`);
            } else if (error.request) {
                // Request was made but no response received
                alert('Network error: No response received from the server');
            } else {
                // Something else happened in setting up the request
                alert(`Error: ${error.message}`);
            }
            console.error(error);
        } finally {
            setLoading(false)
        }

        
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            {/* {loading && <LoadingIndicator />} */}
            <button className="form-button" type="submit">
                {name}
            </button>
        </form>
    );
}

export default Form