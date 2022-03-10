// System imports
import React, { useState, useEffect } from 'react'
import axios from 'axios'

// Third-party imports (please seek permission before installing other libraries)
import { Accordion, AccordionSummary, AccordionDetails } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { CartesianGrid, Legend, Line, LineChart, Tooltip, XAxis, YAxis } from 'recharts';

// Image imports
import headshot from './sample_image.jpeg';
import logoImage from './logo_image.png';
import logoText from './logo_text.png';

// Stylesheet import
import './index.scss';


// Please rename "SampleDashboard" here as well as at the bottom of this file
const SampleDashboard = () => {
    // Please set to unique project identifier (i.e. "energy-dashboard") and do the same in the SCSS file
    let projectName = "PROJECT-NAME-HERE"

    // Sample data to demostrate the recharts library functionality
    const data = [
        {
            "name": "Page A",
            "uv": 4000,
            "pv": 2400,
            "amt": 2400
        },
        {
            "name": "Page B",
            "uv": 3000,
            "pv": 1398,
            "amt": 2210
        },
        {
            "name": "Page C",
            "uv": 2000,
            "pv": 9800,
            "amt": 2290
        },
        {
            "name": "Page D",
            "uv": 2780,
            "pv": 3908,
            "amt": 2000
        },
        {
            "name": "Page E",
            "uv": 1890,
            "pv": 4800,
            "amt": 2181
        },
        {
            "name": "Page F",
            "uv": 2390,
            "pv": 3800,
            "amt": 2500
        },
        {
            "name": "Page G",
            "uv": 3490,
            "pv": 4300,
            "amt": 2100
        }
    ]

    // API call example to fetch data on page load (sets myData to API response)
    const [myData, setMyData] = useState([])
    useEffect(() => {
        axios.get('http://localhost:8000/projects/')
            .then(response => { setMyData(response.data) })
    }, []);


    return (
        // Page content container
        <div className={`${projectName}`}>

            {/* Back button */}
            <span className={`${projectName}__back`}>
                <a href='/'>&lt; Back</a>
            </span>

            {/* Page header */}
            <div className={`${projectName}__header`}>
                <div className={`${projectName}__header-rows`}>
                    <div className={`${projectName}__header-top-row`}>
                        <img className={`${projectName}__header-logo-image`} src={logoImage} />
                        <img className={`${projectName}__header-logo-text`} src={logoText} />
                        <div className={`${projectName}__header-top-row-divider`}><p>|</p></div>
                        <div className={`${projectName}__header-top-row-text`}><p>Design</p></div>
                    </div>
                    <div className={`${projectName}__header-bottom-row`}>
                        <p>Sample Project Name</p>
                    </div>
                </div>
            </div>

            {/* TEAM MEMBERS TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Team Members
                </AccordionSummary>
                <AccordionDetails>
                    <div className={`${projectName}__team-member`}>
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={headshot} />
                            <p className={`${projectName}__team-member-name`}>Sample Name</p>
                            <p>3rd Year Computer Engineering</p>
                            <a href="https://www.linkedin.com">LinkedIn</a>
                        </div>
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={headshot} />
                            <p className={`${projectName}__team-member-name`}>Sample Name</p>
                            <p>3rd Year Computing</p>
                            <a href="https://www.linkedin.com">LinkedIn</a>
                        </div>
                        <div className={`${projectName}__team-member-wrapper`}>
                            <img className={`${projectName}__team-member-headshot`} src={headshot} />
                            <p className={`${projectName}__team-member-name`}>Sample Name</p>
                            <p>4th Year Electrical Engineering</p>
                            <a href="https://www.linkedin.com">LinkedIn</a>
                        </div>
                    </div>
                </AccordionDetails>
            </Accordion>

            {/* PROJECT DESCRIPTION TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Project Description
                </AccordionSummary>
                <AccordionDetails>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                    malesuada lacus ex, sit amet blandit leo lobortis eget.
                </AccordionDetails>
            </Accordion>

            {/* DATA TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Our Data
                </AccordionSummary>
                <AccordionDetails>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                    malesuada lacus ex, sit amet blandit leo lobortis eget.
                </AccordionDetails>
            </Accordion>

            {/* MODEL TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Our Model
                </AccordionSummary>
                <AccordionDetails>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                    malesuada lacus ex, sit amet blandit leo lobortis eget.
                </AccordionDetails>
            </Accordion>

            {/* DEMO TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Demo
                </AccordionSummary>
                <AccordionDetails>
                    <div className={`${projectName}__demo`}>
                        <p>Check out the Recharts API <a href='https://recharts.org/en-US/examples'>here</a>.</p>
                        <div className={`${projectName}__demo-chart-container`}>
                            <p className={`${projectName}__demo-chart-title`}>Demo Chart Title</p>
                            <p className={`${projectName}__demo-chart-desc`}>This is the description for the demo chart.</p>
                            <LineChart width={730} height={250} data={data}
                                margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" />
                                <XAxis dataKey="name" />
                                <YAxis />
                                <Tooltip />
                                <Legend />
                                <Line type="monotone" dataKey="pv" stroke="#8884d8" />
                                <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
                            </LineChart>
                        </div>
                    </div>
                </AccordionDetails>
            </Accordion>

        </div>
    );
}

// Please change to component name decided upon at top of the code
export default SampleDashboard;
