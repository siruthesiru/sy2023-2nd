# Active Directory

Notes for the online [**Introduction to AD DS**](https://learn.microsoft.com/en-us/training/modules/introduction-to-ad-ds/) training course on **Microsoft Certification**'s official site. Lab activities and exam questions will be found here.

## Definition of Terms

- Active Directory
- Schema - set of definitions of object types and attributes that you use to define the objects created in AD DS
- Domain - is a logical administrative container for objects such as users and computers; maps to a partition and is used to organize parent-child relationships
- Domain tree - heirarchical collection of domains that share a common root domain and a contiguous DNS namespace
- Forest - collection of one or more domains that have a common AD DS, root, schema, and global catalog
- OU -
- Container

## What are the Physical Components?

- Domain controller
- Data store
- Global catalog server
- RCDC
- Site
- Subnet

## Group Types

- Security - security-enabled and used for assigning perms to various resources
- Distribution -

## Group scopes

- Local - can only open folders taht are intended for you
- Domain-local - you can access folders in a specific domain
- Global - Within
- Universal - Within

## Trust Relationships

- Parent and child - server and client
- Tree-root - University of San Carlos Domain with sub domains per department
- External - Company branch in the Philippines able to log-into a branch in Kentucky
- Realm - Two forests (Example two Universities) sharing a single library resource
- Forest
- Shortcut

## Organizational Units

Reasons to create organizational units:

- to consolidate objects to make it easier to manage. Example: I have a department and all users have to belong to this department
- To deligate administrative control within the OU. Example: You only allow certain groups to access specific folders within the network

## Default OUs

- Domain
- builtin container
- Computers container
- Foreign security container

## Managing Objects

Using AD Administrative Center

- create and manage users within a domain etc.

---

## Assigment (Individual)

- Create OU for Development, IT, Marketing, Research, Sales
- Create a script that will create users for each organizational unit (5 users each)

## Project

- Create a forest with 3 trees - create the name for each tree/subdomain - Accounting
- Make sure they have trust relationships; any users can log into any domain
- Create four websites on one domain - accounting.powerhouse.com

---

## Notes

> - Each ebsite has its own IP address
> - Add a new user through the command line using the command ```net user newuser password /ADD```
> - create a script using ```.ps1``` scripts and dragging and dropping the file into the PowerShell or CMD window.
> - the active directory has three objects, namely: user, computer, and groups
> - AD DS allows a single domain to contain two billion objects
> - ntop and cerberus look up their relationships
