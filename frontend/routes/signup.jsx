import { Form, redirect } from "react-router-dom"
import { apiCall } from "../src/utils";

const SignUp = () => {
    const handleSignUp = async (event) => {
        console.clear();

        event.preventDefault();

        console.log(event.target.elements['email'].value);

        const SignInInfo = {
            username: event.target.elements['username'].value,
            email: event.target.elements['email'].value,
            password: event.target.elements['password'].value,
        };

        const emailUsed = (await apiCall(`/used-email/${encodeURIComponent(SignInInfo.email)}`, 'GET', null)).response;

        console.log(emailUsed);

        if (emailUsed) {
            alert('Email used!');
            return ;
        };
    };

    return (
        <>
            <h2>Sign up</h2>
            <Form onSubmit={handleSignUp}>
                <input type="username" name="username" placeholder="username" required/>
                <input type="email" name="email" placeholder="email" required/>
                <input type="password" name="password" placeholder="password" required/>
                <input type="submit" />
            </Form>
        </>
    )
};

export default SignUp;