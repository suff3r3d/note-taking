import { redirect} from "react-router-dom"
import { Form } from 'react-bootstrap'
import { apiCall } from "../src/utils";

const SignUp = () => {
    const handleSignUp = async (event) => {
        console.clear();

        event.preventDefault();

        const SignInInfo = {
            username: event.target.elements['username'].value,
            name: event.target.elements['name'].value,
            email: event.target.elements['email'].value,
            password: event.target.elements['password'].value,
        };

        const res = await apiCall('/api/signup', "POST", SignInInfo)
        console.log(res)
    };

    return (
        <div className="flex w-full justify-center text-2xl">
            <div className="w-90 flex bg-blue-200 p-3 items-center rounded-md mt-2 shadow-lg">
                <h2 className="h-auto basis-1/3 text-3xl text-center">Sign up</h2>
                <Form className="ml-2 basis-2/3 w-1/2" onSubmit={handleSignUp}>
                    <div className="grid grid-cols-1 [&_input]:bg-blue-300 [&_input]:rounded-md [&_input]:p-1 [&_input]:shadow-md">
                        <input className="w-full" type="name" name="name" placeholder="name" required/>
                        <input className="w-full mt-2" type="username" name="username" placeholder="username" required/>
                        <input className="w-full mt-2" type="email" name="email" placeholder="email" required/>
                        <input className="w-full mt-2" type="password" name="password" placeholder="password" required/>
                        <input className="w-full mt-2" type="submit" />
                    </div>
                </Form>
            </div>
        </div>
    )
};

export default SignUp;