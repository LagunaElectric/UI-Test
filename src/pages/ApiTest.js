import React, { useState } from 'react';


const ApiTest = () => {
    const [responseData, setResponseData] = useState({message: ""});


    const handleRequest = async () => {
        let response = await fetch("/debug/test_message");
        let data = await response.json()
        setResponseData(await data);
    };
    

    return (
        <div>
            <h1>Api Test Page!</h1>
            <button onClick={handleRequest}>Send Request</button>
            <h2>Response message:</h2>
            <p>{responseData.message}</p>
        </div>
    );
};

export default ApiTest;