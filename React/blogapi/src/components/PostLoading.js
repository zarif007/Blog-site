import React from 'react';


function PostLoading(Componenet) {
    return function PostLoadingComponent({ isLoading, ...props}) {
        if(!isLoading) return <Componenet {...props} />;
        return (
            <p style={{ fontsize: '25px' }}>
                Loading....
            </p>
        )
    }
}

export default PostLoading;