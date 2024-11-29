import { redirect} from "react-router-dom"
import { Form } from 'react-bootstrap'
import { apiCall } from "../src/utils";

const SignIn = () => {
    const handleSignIn = async (event) => {
        event.preventDefault();

        const SignInInfo = {
            username: event.target.elements['username'].value,
            password: event.target.elements['password'].value
        }
    }

    return (
        <div className="flex w-full justify-center text-2xl">
            <div className="w-90 flex bg-blue-200 p-3 items-center rounded-md mt-2 shadow-lg">
                <h2 className="h-auto basis-1/3 text-3xl text-center">Sign in</h2>
                <Form className="ml-2 basis-2/3 w-1/2" onSubmit={handleSignIn}>
                    <div className="grid grid-cols-1 [&_input]:bg-blue-300 [&_input]:rounded-md [&_input]:p-1 [&_input]:shadow-md">
                        <input className="w-full" type="username" name="username" placeholder="username" required/>
                        <input className="w-full mt-2" type="password" name="password" placeholder="password" required/>
                        <input className="w-full mt-2" type="submit" />
                    </div>
                </Form>
            </div>
        </div>
    )
}

export default SignIn;