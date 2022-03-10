// System imports
import React, { useState, useEffect } from 'react'
import axios from 'axios'

// Third-party imports (please seek permission before installing other libraries)
import { Accordion, AccordionSummary, AccordionDetails } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { CartesianGrid, Legend, Line, LineChart, Tooltip, XAxis, YAxis } from 'recharts';
import { useDropzone } from "react-dropzone";

// Image imports
import headshot from './sample_image.jpeg';
import logoImage from './logo_image.png';
import logoText from './logo_text.png';

// Stylesheet import
import './index.scss';


// Please rename "SampleCV" here as well as at the bottom of this file
const SampleCV = () => {
    // Please set to unique project identifier (i.e. "animal-image-classifier") and do the same in the SCSS file
    let projectName = "PROJECT-NAME-HERE"

    // Set default variable values
    const [files, setFiles] = useState([]);
    const [recentImage, setRecentImage] = useState();
    const [reclassify, setReclassify] = useState(false);

    // GET request
    const getImageClass = (obj) => {
        axios
            .get(`http://127.0.0.1:8000/api/images/${obj.data.id}/`, {
                headers: {
                    accept: "application/json",
                },
            })
            .then((resp) => {
                setRecentImage(resp);
                console.log(resp);
            })
            .catch((err) => {
                console.log(err);
            });
    };

    // POST request
    const sendImage = () => {
        let formData = new FormData();
        files[0] && formData.append("picture", files[0], files[0].name);
        axios
            .post("http://127.0.0.1:8000/api/images/", formData, {
                headers: {
                    accept: "application/json",
                    "content-type": "multipart/form-data",
                },
            })
            .then((resp) => {
                getImageClass(resp);
                console.log(resp.data.id);
            })
            .catch((err) => {
                console.log(err);
            });
        setFiles([]);
    };

    // File upload
    const { isDragActive, getRootProps, getInputProps } = useDropzone({
        onDrop: (acceptedFiles) => {
            setFiles(acceptedFiles);
            setReclassify(true);
        },
    });

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

                    {/* Code for a chart, should you wish to use it */}
                    <p>Check out the Recharts API <a href='https://recharts.org/en-US/examples'>here</a>.</p>
                    <div className={`${projectName}__chart-container`}>
                        <p className={`${projectName}__chart-title`}>Demo Chart Title</p>
                        <p className={`${projectName}__chart-desc`}>This is the description for the demo chart.</p>
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
                </AccordionDetails>
            </Accordion>

            {/* DEMO TAB */}
            <Accordion disableGutters>
                <AccordionSummary className={`${projectName}__accordion-heading`} expandIcon={<ExpandMoreIcon />}>
                    Demo
                </AccordionSummary>
                <AccordionDetails>
                    <div className={`${projectName}__demo`}>                        
                        <p className={`${projectName}__demo-title`}>Try it out:</p>
                        {!reclassify && (
                            <div {...getRootProps({ className: "dropzone" })}>
                                <input {...getInputProps()} />
                                <p>
                                    {isDragActive
                                        ? "Drop your image here"
                                        : "Drag and drop an image, or click to select one"}
                                </p>
                            </div>
                        )}

                        <div>
                            <ul className={`${projectName}__demo-images-container`}>
                                {files.map((file) => (
                                    <div>
                                        <img className={`${projectName}__demo-uploaded-image`} src={URL.createObjectURL(file)}/>
                                    </div>
                                ))}
                            </ul>

                            {files.length > 0 && (
                                <button className={`${projectName}__demo-classify-btn`} onClick={sendImage}>
                                    Classify!
                                </button>
                            )}

                            {recentImage && (
                                <div>
                                    <img style={{ maxWidth: 1000 }} src={recentImage.data.picture}/>
                                    <p>Classification result:</p>
                                    <h1>{recentImage.data.classified} </h1>
                                </div>
                            )}

                            {reclassify && (
                                <button
                                    className={`${projectName}__demo-classify-btn`}
                                    onClick={() => {
                                        setReclassify(false);
                                        setFiles([]);
                                        setRecentImage();
                                    }}
                                >Select another image</button>
                            )}
                        </div>
                    </div>
                </AccordionDetails>
            </Accordion>
        </div>
    );
}

// Please change to component name decided upon at top of the code
export default SampleCV;
