import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Outlet } from "react-router-dom"
import './App.scss'
import logo from './Images/logo_text.png';
import Project from './PortfolioProject/index.js'

const App = () => {
    const [projectData, setProjectData] = useState([])

    useEffect(() => {
        axios.get('http://localhost:8000/projects/')
            .then(res => { setProjectData(res.data) })
    }, []);

    return (
        <div>
            <div className="page-content">
            <img className="page-content__logo" src={logo} />
                <div className="page-content__title">
                    <p>Design Team Projects</p>
                </div>
                <div className='page-content__projects'>
                    {projectData.length > 0 ?
                        projectData.map((project) => {
                            return <Project project={project} />
                        })
                        : <p>Loading...</p>

                    }
                </div>
                <Outlet />
            </div>
        </div>
    );
}

export default App;
