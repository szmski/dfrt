
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';
import axios from "axios";
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';

class App extends Component {
    constructor() {
        super();
        this.state = {
            users: []
        }
    }
    getUsers() {
        axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
        .then(res => {this.setState({users: res.data.data.users})})
        .catch(err => {console.log(err)})
    }

    componentDidMount() {
        this.getUsers();        
    }

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-4">
                        <h1>All Users</h1>
                        <br/>
                        <AddUser/>
                        <hr/><br/>
                        <UsersList users={this.state.users}/>
                    </div>
                </div>
            </div>
            )
        }
};
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();