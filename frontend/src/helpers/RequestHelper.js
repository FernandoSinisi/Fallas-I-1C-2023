const getHeader = () => {
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
}

const REQUEST_ERR_LBL = "No pudo realizarse la acción solicitada";

const postTo = (url, body) => {
    return fetch(url, {
            method: "POST",
            headers: getHeader(),
            body: JSON.stringify(body)
        }
    ).then(response =>
        response.json()
    ).catch(error => {
        console.log(error);

        return {
            error: REQUEST_ERR_LBL
        };
    } );
};

const patchTo = (url, body) => {
    return fetch(url, {
            method: "PATCH",
            headers: getHeader(),
            body: JSON.stringify(body)
        }
    ).then(response =>
        response.json()
    ).catch(error => {
        console.log(error);

        return {
            error: REQUEST_ERR_LBL
        };
    } );
};

const getTo = (url) => {
    return fetch(url, {
            method: "GET",
            headers: getHeader()
        }
    ).then(response =>
        response.json()
    ).catch(error => {
        console.log(error);

        return {
            error: REQUEST_ERR_LBL
        };
    } );
};

export {
    postTo, getTo, patchTo
};
