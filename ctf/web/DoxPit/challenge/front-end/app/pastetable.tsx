import React from "react";

import { doRedirect } from "./serverActions";

interface Paste {
    title: string;
    comments: number | string;
    views: number;
    createdBy: string;
    added: string;
}

interface PasteTableProps {
    pastes: Paste[];
    title: string;
    searchQuery: string;
}

const PasteTable: React.FC<PasteTableProps> = ({ pastes, title, searchQuery }) => {
    const filteredPastes = pastes.filter(paste =>
        paste.title.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div>
            <h6 className="text-white">{title}</h6>
            <table className="table table-dark table-striped table-hover">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Comments</th>
                        <th>Views</th>
                        <th>Created by</th>
                        <th>Added</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredPastes.map((paste, index) => (
                        <tr key={index}>
                            <td>
                                <form action={doRedirect}>
                                    <button className="link-light" type="submit">{paste.title}</button>
                                </form>
                            </td>
                            <td>{paste.comments}</td>
                            <td>{paste.views}</td>
                            <td>{paste.createdBy}</td>
                            <td>{paste.added}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PasteTable;
